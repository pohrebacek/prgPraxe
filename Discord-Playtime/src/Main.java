import org.w3c.dom.ls.LSOutput;

import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class Main {

    static HashMap<String, String> gamesMap = new HashMap<>();
    static HashMap<String, Double> timePlayed = new HashMap<>();
    public static void main(String[] args) throws IOException {
        File analyticsFile = new File("E:\\dis2\\Aktivita\\analytics\\events-2026-00000-of-00001.json");
        File reportingFile = new File("E:\\dis2\\Aktivita\\reporting\\events-2026-00000-of-00001.json");
        File tnsFile = new File("E:\\dis2\\Aktivita\\tns\\events-2026-00000-of-00001.json");
        File modelingFile = new File("E:\\dis2\\Aktivita\\modeling\\events-2026-00000-of-00001.json");
        File[] files = {analyticsFile, reportingFile, tnsFile, modelingFile};


        fillGames(files);

        for (Map.Entry<String, String> entry : gamesMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        System.out.println("----------------------------------------------------------------------------");

        getTimePlayed(files);

        for (Map.Entry<String, Double> entry : timePlayed.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue() + "h");
        }

        System.out.println("-----------------------------------------------------------------------------");

        Map<String, Double> sorted = new TreeMap<>(timePlayed);
        System.out.println(sorted);
    }

    public static void fillGames(File[] files) throws IOException {
        BufferedReader br;
        for (File file : files) {
            br = new BufferedReader(new FileReader(file));
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("game_name") && line.contains("game_id")) {
                    String gameName = "";
                    String gameID = "";
                    for (String part : line.split(",")) {
                        if (!gameName.isEmpty() && !gameID.isEmpty()) {
                            break;
                        }
                        if (part.contains("game_name\"")) {
                            System.out.println(part);
                            String partValue = part.split("\":\"")[1];
                            gameName = partValue.substring(0, partValue.length()-1);
                        }
                        if (part.contains("game_id\"")) {
                            System.out.println(part);
                            String partValue = part.split("\":\"")[1];
                            gameID = partValue.substring(0, partValue.length()-1);
                        }
                    }
                    gamesMap.put(gameID, gameName);
                }
            }

        }
    }

    public static void getTimePlayed (File[] files) throws IOException {
        BufferedReader br;
        for (File file : files) {
            br = new BufferedReader(new FileReader(file));
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("application_id") && line.contains("total_duration_s")) {
                    String gameID = "";
                    String gameName = "";
                    double totalDuration = -1.0;
                    for (String part : line.split(",")) {
                        if (!gameID.isEmpty() && totalDuration != -1.0) {
                            break;
                        }
                        if (part.contains("application_id")) {
                            String partValue = part.split("\":\"")[1];
                            gameID = partValue.substring(0, partValue.length()-1);
                            gameName = gamesMap.get(gameID);
                        }
                        if (part.contains("total_duration_s")) {
                            String partValue = part.split("\":\"")[1];
                            double totalDurationSeconds = Double.parseDouble(partValue.substring(0, partValue.length()-1));
                            totalDuration = totalDurationSeconds / 3600;
                        }
                    }
                    if (timePlayed.get(gameName) == null || timePlayed.get(gameName) < totalDuration) {
                        timePlayed.put(gameName, totalDuration);
                    }
                }
            }
            br.close();
        }
    }
}
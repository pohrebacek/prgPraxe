from app import create_app, db, sio, sio_app

if __name__ == "__main__":
    app = create_app()


    import eventlet
    eventlet.wsgi.server(eventlet.listen(('', 5000)), sio_app(app))

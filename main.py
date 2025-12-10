import acggiftart
import config

# Create the Flask app using acggiftart
app = acggiftart.create_app(config)

# This block is only used when running locally. Gunicorn runs the application in production.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
  # defining GET
  def get(self):
    # setting the return
    # python dictionary, key and values // data and helloworld
    # you want to return json serializable objects // use python dictionareis like below
    return {"data": "hello world"}

# where you can access the GET from // how you find it
# Get request to /helloworld should yield "hello world"
api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
  # only for dev enviornment, do not run in production
  app.run(debug=True)
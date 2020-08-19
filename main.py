from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
# making a dictionary
names = {"nick": {"age": 30, "gender": "male"},
        "danielle": {"age": 26, "gender": "female"}}

class HelloWorld(Resource):
  # defining GET
  def get(self, name):
    # setting the return
    # python dictionary, key and values // data and helloworld
    # you want to return json serializable objects // use python dictionareis like below
    return {"name": name}

# where you can access the GET from // how you find it
# Get request to /helloworld should yield "hello world"
# use <> to define parameters in the path
api.add_resource(HelloWorld, "/helloworld<string:name>")

if __name__ == "__main__":
  # only for dev enviornment, do not run in production
  app.run(debug=True)
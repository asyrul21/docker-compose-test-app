from flask_restful import Resource


class Index(Resource):
    # restful automatically maps method name to request type
    def get(self):
        return {
            'message': 'Index Page of the Spacy Embeddings API'
        }

    def post(self):
        return {
            'message': 'You have made a POST request!'
        }

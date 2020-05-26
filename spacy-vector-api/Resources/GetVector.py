from flask_restful import Resource, reqparse
from flask_restful import fields, marshal_with
from markupsafe import escape


# define arguments parser
# reqparse is Resource specific
# i.e. args defined in here does not work in other Resources
parser = reqparse.RequestParser()
parser.add_argument('sentence', type=str,
                    help='Input sentence')


class GetVector(Resource):
    def __init__(self, wordEmbedder):
        self.wordEmbedder = wordEmbedder

    def get(self, ):
        # get input
        message = parser.parse_args()['sentence']

        # escape input message
        escapedMessage = str(escape(message))

        # get vector
        res = self.wordEmbedder.getVector(escapedMessage)
        print('Res:', res)
        print('Shape:', res.shape)

        # return response as json
        return {
            "vector": res.tolist(),
        }

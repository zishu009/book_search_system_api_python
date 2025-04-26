from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    genre = fields.Str(required=True)
    year = fields.Int(required=True)

class PromptSchema(Schema):
    prompt = fields.Str(required=True)

# Initialize schemas
book_schema = BookSchema()
books_schema = BookSchema(many=True)
prompt_schema = PromptSchema()
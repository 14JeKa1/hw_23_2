from marshmallow import Schema, fields

# Список валидных команд
#VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort')

class RequestSchema(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)

# V2
#class RequestSchema(Schema):
#    cmd = fields.Str(required=True)
#    value = fields.Str(required=True)

#class BatchRequestSchema(Schema):
#    queries = fields.Nested(RequestSchema, many=True)
#    file_name = fields.Str(required=True)
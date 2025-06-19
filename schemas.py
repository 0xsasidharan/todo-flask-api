from marshmallow import Schema , fields

class TaskSchema(Schema):
    task_id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    due_date = fields.Str(required=True)
    description = fields.Str()
    completed = fields.Bool(load_default=False)
    created_at = fields.Str(dump_only=True)

class TaskUpdateSchema(Schema):
    name = fields.Str()
    due_date = fields.Str()
    description = fields.Str()
    completed = fields.Bool()

import json

from flask import Blueprint, request, jsonify, Response, Union

from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, tuple[Response, int]]:

     #TODO: Принять запрос от пользователя
      data = request.json
    # TODO: Обработать запрос, валидировать значения
    # try:
    #     validated_data = RequestSchema().load(data)
    # except ValueError as error:
    #     return Response(
    #         response=json.dumps(error.messages_doct),
    #         status=400,
    #         content_type='application/json',
    #     )
    #  return jsonify(error.messages), 400
    # TODO: Выполнить запрос
    # first_result = build_query(
    #     cmd=data['cmd1'],
    #     value=data['value1'],
    #     file_name=data['file_name'],
    #     data=None,
    # )
    # second_result = build_query(
    #     cmd=data['cmd2'],
    #     value=data['value2'],
    #     file_name=data['file_name'],
    #     data=first_result,
    # return jsonify(second_result)

    # V2
    # result: Optional[list[str]] = None
    # for query in validated_data['queries']:
    #     result = build_query(
    #         cmd=query['cmd'],
    #         value=query['value'],
    #         file_name=validated_data['file_name'],
    #         data=result,
    #     )

    # return jsonify(result)


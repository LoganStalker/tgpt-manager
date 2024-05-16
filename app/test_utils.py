import json


def test_get_bots_list(httpx, response, backend):
    bot_obj = {
        'id': 1,
        'bot_name': 'Bot1',
        'bot_token': 'as123sdff43',
        'bot_api_id': '12345564234',
        'bot_api_hash': 'adsdazc123123132',
        'openai_api_key': 'rtterterte-trtetertlkmlmk;tr',
        'openai_organization': 'xcvxcvxcfdfgdfg',
        'openai_assistant_id': 'asdasdasdasdasd',
        'active': True
    }

    httpx.return_value = response(json=[bot_obj])

    res = backend.get_bots_list()
    assert res == [bot_obj]

    assert httpx.called

    ((req), ), _ = httpx.call_args
    assert req.method == "GET"
    assert req.url.path == "/bots"
    assert req.url.host == "127.0.0.1"


def test_create_bot(httpx, backend):
    data = {
        'bot_name': 'Bot1',
        'bot_token': 'as123sdff43',
        'bot_api_id': '12345564234',
        'bot_api_hash': 'adsdazc123123132',
        'openai_api_key': 'rtterterte-trtetertlkmlmk;tr',
        'openai_organization': 'xcvxcvxcfdfgdfg',
        'openai_assistant_id': 'asdasdasdasdasd',
    }

    backend.create_bot(data)

    assert httpx.called

    ((req), ), params = httpx.call_args
    assert req.method == "POST"
    assert req.url.path == "/bots"
    assert json.loads(req.read()) == data

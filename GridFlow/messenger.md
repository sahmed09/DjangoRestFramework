## Messenger APIs
```
http://54.251.167.179:8000/api/messenger/
```

### Conversation API:
http://54.251.167.179:8000/api/messenger/conversation_api/ <br>
Required fields: name <br>
Example:
```
{
    "name": "gridflow"
}
```
Output:
```
{
    "id": 1,
    "name": "gridflow"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/messenger/conversation_api/?name=gridflow
Output:
[
    {
        "id": 1,
        "name": "gridflow"
    }
]
```

### ConversationMember API:
http://54.251.167.179:8000/api/messenger/conversation_member_api/ <br>
Required fields: conversation, user <br>
Example:
```
{
    "conversation": {"name": "gridflow"},
    "user": {"username": "admin"}
}
```
Output:
```
{
    "id": 5,
    "conversation": 1,
    "user": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/messenger/conversation_member_api/?conversation__name=gridflow
Output:
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 5,
            "conversation": 1,
            "user": 1
        },
        {
            "id": 6,
            "conversation": 1,
            "user": 2
        }
    ]
}
```

### Message API:
http://54.251.167.179:8000/api/messenger/message_api/ <br>
Required fields: conversation, user, msg <br>
Optional field: attachment <br>
Example:
```
{
    "conversation": {"name": "gridflow"},
    "user": {"username": "admin"},
    "msg": "Hello from Admin"
}
```
Output:
```
{
    "id": 31,
    "msg": "Hello from Admin",
    "attachment": null,
    "timestamp": "2021-10-29T20:33:51.470881",
    "conversation": 1,
    "user": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/messenger/message_api/?conversation__name=gridflow
Output:
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 31,
            "msg": "Hello from Admin",
            "attachment": null,
            "timestamp": "2021-10-29T20:33:42.133884",
            "conversation": 1,
            "user": 1
        },
        {
            "id": 32,
            "msg": "Hello from Admin 2",
            "attachment": null,
            "timestamp": "2021-10-29T20:33:51.470881",
            "conversation": 1,
            "user": 1
        }
    ]
}
```

```
Models:
Conversation: Creates a conversation.
ConversationMember: Add members to a specific conversation.
Message: Stores messages of a specific conversation. Also shows those messages using websocket.
    A signal (conversations) is generated if a message is stored.
MessageSeenStatus: status=True if a message of a conversation is seen.
```

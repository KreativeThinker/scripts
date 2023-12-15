S = \
{
	"type" : "aa{sv}",
	"data" : [
		[
			{
				"body" : {
					"type" : "s",
					"data" : "My old friend. I have come to talk with you again"
				},
				"message" : {
					"type" : "s",
					"data" : "<b>Hello darkness</b>\nMy old friend. I have come to talk with you again"
				},
				"summary" : {
					"type" : "s",
					"data" : "Hello darkness"
				},
				"appname" : {
					"type" : "s",
					"data" : "dunstify"
				},
				"category" : {
					"type" : "s",
					"data" : ""
				},
				"default_action_name" : {
					"type" : "s",
					"data" : "default"
				},
				"icon_path" : {
					"type" : "s",
					"data" : ""
				},
				"id" : {
					"type" : "i",
					"data" : 6
				},
				"timestamp" : {
					"type" : "x",
					"data" : 4265705280
				},
				"timeout" : {
					"type" : "x",
					"data" : 10000000
				},
				"progress" : {
					"type" : "i",
					"data" : -1
				}
			},
			{
				"body" : {
					"type" : "s",
					"data" : "My old friend"
				},
				"message" : {
					"type" : "s",
					"data" : "<b>Hello darkness</b>\nMy old friend"
				},
				"summary" : {
					"type" : "s",
					"data" : "Hello darkness"
				},
				"appname" : {
					"type" : "s",
					"data" : "dunstify"
				},
				"category" : {
					"type" : "s",
					"data" : ""
				},
				"default_action_name" : {
					"type" : "s",
					"data" : "default"
				},
				"icon_path" : {
					"type" : "s",
					"data" : ""
				},
				"id" : {
					"type" : "i",
					"data" : 5
				},
				"timestamp" : {
					"type" : "x",
					"data" : 4255400254
				},
				"timeout" : {
					"type" : "x",
					"data" : 10000000
				},
				"progress" : {
					"type" : "i",
					"data" : -1
				}
			},
			{
				"body" : {
					"type" : "s",
					"data" : ""
				},
				"message" : {
					"type" : "s",
					"data" : "<b>Helloas</b>"
				},
				"summary" : {
					"type" : "s",
					"data" : "Helloas"
				},
				"appname" : {
					"type" : "s",
					"data" : "dunstify"
				},
				"category" : {
					"type" : "s",
					"data" : ""
				},
				"default_action_name" : {
					"type" : "s",
					"data" : "default"
				},
				"icon_path" : {
					"type" : "s",
					"data" : ""
				},
				"id" : {
					"type" : "i",
					"data" : 4
				},
				"timestamp" : {
					"type" : "x",
					"data" : 972469284
				},
				"timeout" : {
					"type" : "x",
					"data" : 10000000
				},
				"progress" : {
					"type" : "i",
					"data" : -1
				}
			},
			{
				"body" : {
					"type" : "s",
					"data" : ""
				},
				"message" : {
					"type" : "s",
					"data" : "<b>Helloa</b>"
				},
				"summary" : {
					"type" : "s",
					"data" : "Helloa"
				},
				"appname" : {
					"type" : "s",
					"data" : "dunstify"
				},
				"category" : {
					"type" : "s",
					"data" : ""
				},
				"default_action_name" : {
					"type" : "s",
					"data" : "default"
				},
				"icon_path" : {
					"type" : "s",
					"data" : ""
				},
				"id" : {
					"type" : "i",
					"data" : 3
				},
				"timestamp" : {
					"type" : "x",
					"data" : 970915297
				},
				"timeout" : {
					"type" : "x",
					"data" : 10000000
				},
				"progress" : {
					"type" : "i",
					"data" : -1
				}
			},
			{
				"body" : {
					"type" : "s",
					"data" : ""
				},
				"message" : {
					"type" : "s",
					"data" : "<b>Hello</b>"
				},
				"summary" : {
					"type" : "s",
					"data" : "Hello"
				},
				"appname" : {
					"type" : "s",
					"data" : "dunstify"
				},
				"category" : {
					"type" : "s",
					"data" : ""
				},
				"default_action_name" : {
					"type" : "s",
					"data" : "default"
				},
				"icon_path" : {
					"type" : "s",
					"data" : ""
				},
				"id" : {
					"type" : "i",
					"data" : 2
				},
				"timestamp" : {
					"type" : "x",
					"data" : 969356343
				},
				"timeout" : {
					"type" : "x",
					"data" : 10000000
				},
				"progress" : {
					"type" : "i",
					"data" : -1
				}
			}
		]
	]
}
for i in S["data"][0]:
    print(i["appname"]["data"])
    print(i["summary"]["data"])
    print("------------------")

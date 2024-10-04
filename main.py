import req

model_list = []
prompt = input()

for model in model_list:
    print("Asking {model}")
    output_file = open("{model}.txt", "w+")
    output_file.write(req.req(model, prompt, account_id, api_token))
    output_file.close()

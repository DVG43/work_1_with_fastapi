from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"key": "hello"}


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

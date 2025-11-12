from fastapi import FastAPI, HTTPException
import uvicorn
import json
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    id : int
    name : str
    price : float


def load_data():
    with open("data.json") as json_file:
        data = json.load(json_file)
        return data


def save_data(data):
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


@app.get("/items/")
def get_all_items():
    return load_data()


@app.put("/items/")
def get_item(item: Data):
    data = load_data()
    for i in data:
        if i["id"] == item.id:
            i["price"] = item.price
        save_data(data)
        return 787
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

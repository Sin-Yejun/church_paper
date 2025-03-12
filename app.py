from flask import Flask, request, jsonify

app = Flask(__name__)

def read_image_url():
    try:
        with open("img_url.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "아직 주보 이미지가 저장되지 않았습니다."

@app.route('/skill', methods=['POST'])
def skill():
    # 카카오톡에서 보내주는 요청 데이터 받기
    data = request.get_json()
    user_input = data['userRequest']['utterance'].strip()

    # "주보"일 때만 이미지 URL 읽기
    if user_input == "주보":
        img_url = read_image_url()
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": "주보 이미지",
                            "thumbnail": {
                                "imageUrl": img_url
                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "이미지 보기",
                                    "webLinkUrl": img_url
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else:
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            f"text": " '주보'라고 입력하면 주보 이미지를 보여드립니다!"
                        }
                    }
                ]
            }
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
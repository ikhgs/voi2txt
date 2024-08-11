from flask import Flask, request, jsonify
import assemblyai as aai

app = Flask(__name__)

aai.settings.api_key = "3878eb378b12473bbf4abaf43f5e6a38"
transcriber = aai.Transcriber()

@app.route('/voice2txt', methods=['GET'])
def voice_to_text():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        transcript = transcriber.transcribe(video_url)
        return jsonify({"transcript": transcript.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

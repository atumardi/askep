from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"

def generate_report(diagnosis):
  prompt = f"Buat laporan pendahuluan asuhan keperawatan untuk pasien dengan diagnosis {diagnosis}. Laporan harus mengikuti sistematika penulisan yang lengkap, termasuk bab pendahuluan, tinjauan teoritis, dan rencana asuhan keperawatan. Fokus pada konsep dasar medis dan keperawatan yang relevan."
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
  )
  return response.choices[0].text

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    diagnosis = request.form['diagnosis']
    report = generate_report(diagnosis)
    # Simpan report dalam file Word atau PDF
    # Kirimkan link download ke pengguna
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)

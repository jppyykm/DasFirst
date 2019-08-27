from flask import Flaski
import keras.models import load_model
from keras.applications.resnet10 import ResNet50

app = Flask(__name__)
model = ResNet50(weights='imagenet')
MODEL_PATH = 'models/your_model.h5'

@app.route('/')
def index():
    return render_template('index.html')


def model_predict(img_path, model):
    img = image.load_img(imp_path)
    x = image.img_to_array(img)
    preds = model.predict(x)
    return preds


@app.route('/predict')


def upload():
    if request.method =='POST':
        f = request.files['file']
        f.save(file_path)
        preds = model_predict(file_path, model)
        pred_class = decode_predictions(preds, top=1)
    return pred_class



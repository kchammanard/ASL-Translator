import cv2
import math
import time
import os
import string
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from track import HandTracking

model = load_model("asl_model/baseline_model_2.h5",compile= False)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(),
                       tf.keras.metrics.FalseNegatives()])

cap = cv2.VideoCapture(0)
offset = 20
imgSize = 300
classes = dict( (i, key) for i,key in enumerate(string.ascii_lowercase))

sentence = []

def hands_feed():
    HT = HandTracking()

    count = 0
    color = (0, 0, 255)

    # capture from live web cam
    cap = cv2.VideoCapture(0)
    frame_width, frame_height = int(cap.get(3)), int(cap.get(4))

    start = time.time()
    pred = "No predictions"
    prev_pred = None
    l = []
    while cap.isOpened():
        insert = False

        ret, frame = cap.read()
        if not ret:
            print("Ignoring empty camera frame.")
            continue

        image = frame.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # hand tracking
        hands_results = HT.track(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # init frame each loop
        HT.read_results(image, hands_results)

        l = []
        if hands_results.multi_hand_landmarks:
            HT.draw_hand()
            HT.draw_hand_label()

            hand = hands_results.multi_hand_landmarks[0]
            for i in range(21):
                l += HT.get_moy_coords(hand, i)

            # sl = ",".join(map(str, l))
            # print(sl)
        else: 
            pred = "No predictions"

        if len(l) == 0:
            pred = ""
        else:
            a = np.array([l])
            p = model.predict(a)    
            p_index = np.argmax(p, axis=1)
            pred = classes[int(str(p_index)[1:-1])]
        
        # print("prev pred:", prev_pred)
        # print("pred:",pred)

        if prev_pred == pred:
            count += 1
            if count >= 10:
                color = (0,255,0)
                count = 0
                insert = True
        else:
            count = 0
            prev_pred = None
            color = (0,0,255)

        if pred != "No predictions":
            prev_pred = pred
        
        if insert:
            print("LETTER ADDED TO SENTENCE")
            sentence.append(pred)

        print(insert)

        cv2.putText(image, "".join(sentence) + pred, (10, frame_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    color, 2)

        cv2.imshow("image", image)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    hands_feed()

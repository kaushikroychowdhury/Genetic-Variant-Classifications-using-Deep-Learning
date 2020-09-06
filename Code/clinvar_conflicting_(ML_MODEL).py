# Importing relevant libraries
import numpy as np
import tensorflow as tf

# DATA
npz = np.load("clinvar_conflicting_train.npz")

train_inputs = npz["inputs"].astype(np.float)
train_targets = npz["targets"].astype(np.int)

npz = np.load("clinvar_conflicting_validation.npz")

validation_inputs = npz["inputs"].astype(np.float)
validation_targets = npz["targets"].astype(np.int)

npz = np.load("clinvar_conflicting_test.npz")

test_inputs = npz["inputs"].astype(np.float)
test_targets = npz["targets"].astype(np.int)

# Model (Outline, optimizer, loss function, Training )

input_size = 9
output_size = 2
hidden_layer_size = 200

## Outline the model

model = tf.keras.Sequential([
    tf.keras.layers.Dense(hidden_layer_size, activation = 'relu'),
    tf.keras.layers.Dense(hidden_layer_size, activation = 'relu'),
    # tf.keras.layers.Dense(hidden_layer_size, activation = 'relu'),
    # tf.keras.layers.Dense(hidden_layer_size, activation = 'relu'),
    # tf.keras.layers.Dense(hidden_layer_size, activation = 'relu'),
    # tf.keras.layers.Dense(hidden_layer_size, activation = 'relu'),
    # tf.keras.layers.Dense(hidden_layer_size, activation = 'relu'),
    tf.keras.layers.Dense(output_size, activation = 'softmax')
])

# Optimizer

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss= 'sparse_categorical_crossentropy', metrics=['accuracy'])

# Training

batch_size = 100
max_epoch = 100

early_stopping = tf.keras.callbacks.EarlyStopping(patience=2)

#fit the model

model.fit(train_inputs, train_targets, batch_size= batch_size, epochs= max_epoch,
          validation_data=(validation_inputs, validation_targets),
          callbacks=[early_stopping], verbose = 2)

### TEST THE MODEl

test_loss , test_accuracy = model.evaluate(test_inputs, test_targets)
print('Test loss : {0:.2f}    Test accuracy : {1:.2f}%'.format(test_loss, test_accuracy*100.))



#### Accuracy 77%
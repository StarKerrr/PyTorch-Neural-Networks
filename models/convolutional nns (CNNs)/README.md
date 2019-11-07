# What is Convolutional Neural Networks (CNN) ?
### What is it and what is it used for
&nbsp;&nbsp;&nbsp;The convolutional neural network, or CNN for short, is a specialized type of neural network model designed for working with two-dimensional image data, although they can be used with one-dimensional and three-dimensional data.

&nbsp;&nbsp;&nbsp;Central to the convolutional neural network is the convolutional layer that gives the network its name. So, what does it mean and how does it work in networks of this type. This layer performs an operation called a “convolution“, i.e. reducing the size of something, making dimension of data smaller. In the context of a convolutional neural network, a convolution is a linear operation that involves the multiplication of a set of weights with the input, much like a traditional neural network. Given that the technique was designed for two-dimensional input, the multiplication is performed between an array of input data and a two-dimensional array of weights, called a filter or a kernel. The filter is smaller than the input data and the type of multiplication applied between a filter-sized patch of the input and the filter is a dot product.

&nbsp;&nbsp;&nbsp;This is a fancy mathematical word for what is essentially a moving window or filter across the image being studied. This moving window applies to a certain neighborhood of nodes as shown below (imagine that cells are the pixels of image).

![](/res/convolutional-nns-(CNNs)/convolution_schematic.gif)

&nbsp;&nbsp;&nbsp;So, it is the main approach to convolve a given dataset. This systematic application of the same filter across an image is a powerful idea. If the filter is designed to detect a specific type of feature in the input, then the application of that filter systematically across the entire input image allows the filter an opportunity to discover that feature anywhere in the image.

&nbsp;&nbsp;&nbsp;There are a few things in this convolutional step which improve training by reducing parameters/weights:
* Sparse connections – not every node in the first / input layer is connected to every node in the second layer. This is contrary to fully connected neural networks, where every node is connected to every other in the following layer;
* Constant filter parameters – each filter has constant parameters. In other words, as the filter moves around the image, the same weights are applied to each 2 x 2 set of nodes. Each filter, as such, can be trained to perform a certain specific transformation of the input space. Therefore, each filter has a certain set of weights that are applied for each convolution operation – this reduces the number of parameters.

### Activation function
&nbsp;&nbsp;&nbsp;The next step in the Convolutional Neural Network structure is to pass the output of the convolution operation through a non-linear activation function – generally some version of the ReLU activation function. ReLU stands for Rectified Linear Unit for a non-linear operation. The output is ƒ(x) = max(0,x). Why ReLU is important: ReLU’s purpose is to introduce non-linearity in our ConvNet. Since, the real world data would want our ConvNet to learn would be non-negative linear values. How does it look:

![](/res/convolutional-nns-(CNNs)/relu_activation_function.png)

### Pooling
&nbsp;&nbsp;&nbsp;So, the next vitally important part of Convolutional Neural Networks is a concept called pooling. There are two benefits of pooling:
* It reduces the number of parameters in your model by a process called down-sampling;
* It makes feature detection more robust to object orientation and scale changes.

&nbsp;&nbsp;&nbsp;So what is pooling? It is another sliding window type technique, but instead of applying weights, which can be trained, it applies a statistical function of some type over the contents of its window. The most common type of pooling is called max pooling, and it applies the max() function over the contents of the window.

![](/res/convolutional-nns-(CNNs)/max_pooling.jpg)

### Strides and down-sampling
&nbsp;&nbsp;&nbsp;Stride is the number of pixels shifts over the input matrix. When the stride is 1 then we move the filters to 1 pixel at a time. When the stride is 2 then we move the filters to 2 pixels at a time and so on. In the pooling diagram above, you will notice that the pooling window shifts to the right each time by 2 places. One important thing to notice is that, if during pooling the stride is greater than 1, then the output size will be reduced. As can be observed above, the 5 x 5 input is reduced to a 3 x 3 output. This is a good thing – it is called down-sampling, and it reduces the number of trainable parameters in the model.

### Padding
&nbsp;&nbsp;&nbsp;When 2 x 2 pooling window can't operate correctly with a stride of [2, 2] and filter does not fit perfectly fit the input image an extra column is added to matrix of data and is called padding. The nodes of this column are basically dummy nodes – because the values of these dummy nodes is 0, they are basically invisible to the max pooling operation.

![](/res/convolutional-nns-(CNNs)/padding_image.png)

### Fully connected layer
&nbsp;&nbsp;&nbsp;As previously discussed, a Convolutional Neural Network takes high resolution data and effectively resolves that into representations of objects. The fully connected layer can therefore be thought of as attaching a standard classifier onto the information-rich output of the network, to “interpret” the results and finally produce a classification result. We flattened our matrix into vector and feed it into a fully connected layer like neural network. With the fully connected layers, we combined the features together to create a model.

![](/res/convolutional-nns-(CNNs)/fully_connected_layer.png)

### Inference
&nbsp;&nbsp;&nbsp;I hope this article was useful for you and you found out something new and important in understanding Convolutional Neural Networks. Now, check out code implementation of CNN in PyTorch, maybe the code could say more than words :)                
&nbsp;&nbsp;&nbsp;Image below personifies all that we are talking about.

![](/res/convolutional-nns-(CNNs)/typical_cnn.png)
###### (The image has been taken from Wikipedia)

---
If you haven't experienced this task before and you want to go deeper, understandable and well-orginized information can be taken [HERE](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148) and [HERE](https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/).

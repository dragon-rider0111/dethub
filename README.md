<div align="center">
<h1>
DetHub: Object Detection Model Hub
</h1>
<img src="doc/torchvision.jpg" alt="Torchvision" width="800">
</div>

### Yolov5 Object Prediction and Visualization
```
run('yolov5', 'dethub/models/yolov5/yolov5n.pt', 'data/highway1.jpg')
```
<img src="doc/yolov5.jpg" alt="Yolov5" width="800">

### Torchvision Object Prediction and Visualization
```
run("torchvision", "dethub/models/torchvision/fasterrcnn_resnet50_fpn.pth", "data/highway1.jpg")
```
<img src="doc/torchvision.jpg" alt="Torchvision" width="800">

### TfHub Object Prediction and Visualization
```
run('tensorflow', 'https://tfhub.dev/tensorflow/efficientdet/d3/1', 'data/highway1.jpg')
```
<img src="doc/tensorflow.jpg" alt="TfHub" width="800">

## TODO
- [ ] Detectron2 will be added.
- [ ] Hugging Face will be added.

References:
- [SAHI](https://github.com/obss/sahi)
- [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)

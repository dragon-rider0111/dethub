from dethub.model import *


def pretrained_weights():
    from dethub.utils.file_utils import ModelDownload

    ModelDownload.yolov5n()
    ModelDownload.torchvision()


def get_prediction(image, detection_model):
    import cv2

    from dethub.utils.visualize import vis

    image = cv2.imread(image)
    object_prediction_list = detection_model.object_prediction_list(image)
    vis(image, object_prediction_list)


def run(model_type, model_path, image_path, device="cpu", confidence_threshold=0.5):
    if model_type == "yolov5":
        detection_model = Yolov5(model_path, device, confidence_threshold)

    elif model_type == "torchvision":
        detection_model = TorchVision(model_path, device, confidence_threshold)

    elif model_type == "tensorflow":
        detection_model = TensorflowHub(model_path, device, confidence_threshold)

    get_prediction(image_path, detection_model)


# run('yolov5', 'dethub/models/yolov5/yolov5n.pt', 'data/highway1.jpg')
# run("torchvision", "dethub/models/torchvision/fasterrcnn_resnet50_fpn.pth", "data/highway1.jpg")
# run('tensorflow', 'https://tfhub.dev/tensorflow/efficientdet/d3/1', 'data/highway1.jpg')

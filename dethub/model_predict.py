def torchvision_prediction(img, model_path, confidence_threshold):
    from dethub.utils.data_utils import read_image, numpy_to_torch, torch_to_numpy, COCO_CLASSES
    from dethub.utils.file_utils import download_torchvision_model
    import torchvision,torch

    download_torchvision_model()
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model.load_state_dict(torch.load(model_path))
    model.eval()

    img = read_image(img)
    img = numpy_to_torch(img)
    prediction = model([img])
    img = torch_to_numpy(img)
    prediction_class = [COCO_CLASSES[i] for i in list(prediction[0]['labels'].numpy())]
    prediction_boxes = [[(i[0], i[1]), (i[2], i[3])] for i in list(prediction[0]['boxes'].detach().numpy())]
    prediction_score = list(prediction[0]['scores'].detach().numpy())
    prediction_thresh = [prediction_score.index(x) for x in prediction_score if x > confidence_threshold][-1]
    prediction_boxes = prediction_boxes[:prediction_thresh + 1]
    prediction_class = prediction_class[:prediction_thresh + 1]
    return img ,prediction_boxes, prediction_class, prediction_score

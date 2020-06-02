# darknet-ocr-wrap

[chineseocr/darknet-ocr] 的封装 | a wrap for [chineseocr/darknet-ocr]

https://github.com/chineseocr/darknet-ocr

## ocr-heroku

免费部署 [chineseocr/darknet-ocr] 服务| deploy [chineseocr/darknet-ocr] on heroku for free

```
cd ocr-heroku
docker build -t web .
heroku login
heroku create
heroku container:login
heroku container:push web
heroku container:release web
heroku ps:scale web=1
```

## ocr-image

识别图片并输出 JSON 结果 | OCR image and output JSON results

```
docker run --rm \
  -e OCR_IMAGE_PATH=/tmp/test.png
  -v $pwd/test.png:/tmp/test.png
  postor/darknet-ocr:1.0-image
```

结果示例 | example output

```
[{"text": "f", "prob": 1.0, "chars": [{"char": "f", "prob": 1.0}], "box": [208, 4, 246, 8, 242, 42, 204, 38], "textprob": 0.76}, {"text": "N", "prob": 1.0, "chars": [{"char": "N", "prob": 1.0}], "box": [13, 7, 59, 6, 60, 43, 14, 45], "textprob": 0.9}, {"text": ".", "prob": 1.0, "chars": [{"char": ".", "prob": 1.0}], "box": [56, 28, 94, 5, 109, 30, 71, 53], "textprob": 0.71}]
```
from transformers import pipeline

captioner = pipeline(
    "image-to-text",
    model="ydshieh/vit-gpt2-coco-en"
)

image_path = input("Enter image path: ")

result = captioner(image_path)

print("\nGenerated Caption:")
print(result[0]["generated_text"])
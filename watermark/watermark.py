# create a script that adds a watermark to an image stored in an AWS s3 instance and saves the new image in the s3 instance
import boto3
from PIL import Image

def add_watermark(raw_file, watermark_file, outfile, transparent = True):
    """Adds watermark to an image and saves the image in a new file."""
    # load images
    image = Image.open(raw_file)
    watermark = Image.open(watermark_file)
    # position calculation
    position = (image.size[0] - watermark.size[0], image.size[1] - watermark.size[1])
    if transparent:
        transparent_img = Image.new("RGBA", image.size, (0,0,0,0))
        transparent_img.paste(image, (0,0))
        transparent_img.paste(watermark, position, mask=watermark)
        transparent_img.save(outfile)
    else:
        # place watermark and save to new file
        image.paste(watermark, position)
        image.save(outfile)
    

def main():
    """Downloading an image file from S3, adding a watermark, and uploading it to a new prefix in S3.""" 
    bucket_name = "cluut-aws-developer-kurs-benjamin-wieland-02-05-2023"
    file_name = "programming_coffee.png"
    key = "raw/" + file_name
    
    # Download file
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, key, file_name)
    # Add watermark
    outfile = file_name.replace(".png", "_finale.png")
    add_watermark(file_name, "watermark.png", outfile)
    # Upload final image
    s3.upload_file(outfile, bucket_name, "final/"+outfile)
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
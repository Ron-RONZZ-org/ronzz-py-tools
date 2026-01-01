import argparse
import os
import pdfplumber


def extract_images_from_pdf(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            for image_index, image in enumerate(page.images, start=1):
                # Extract image bounding box
                bbox = image["x0"], image["top"], image["x1"], image["bottom"]
                cropped_image = page.within_bbox(bbox).to_image()

                # Save image as PNG
                document_name = os.path.splitext(os.path.basename(pdf_path))[0]
                image_name = (
                    f"{document_name}_page_{page_number}_image_{image_index}.png"
                )
                image_path = os.path.join(output_dir, image_name)
                cropped_image.save(image_path, format="PNG")
                print(f"Saved: {image_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract all images from a PDF and save them as PNG files."
    )
    parser.add_argument("pdf_path", help="Path to the input PDF file.")
    parser.add_argument(
        "output_dir", help="Directory to save the extracted PNG images."
    )
    args = parser.parse_args()

    extract_images_from_pdf(args.pdf_path, args.output_dir)


if __name__ == "__main__":
    main()

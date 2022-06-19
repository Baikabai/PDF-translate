import pic
import ocrrecognize


if __name__ == "__main__":
    pdffile = 'C:/Users/umiko/Desktop/baikabai/PDF_PIC/pdf/テキストマイニングを利用した テーマに関連する上場企業検索ツールの開発.pdf'
    imagePath = 'C:/Users/umiko/Desktop/baikabai/PDF_PIC/image'
    pic.pyMuPDF_fitz(pdffile, imagePath)
    ocrrecognize.recognize_text(imagePath)
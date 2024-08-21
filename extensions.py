def main():
    inputstring = input("Enter any filename with extension:  ").lower()
    outputstring = inputstring.rpartition(".")[2]

    match(outputstring):
        case "gif":
            ext = "image/gif"
        case 'jpg' | 'jpeg':
            ext = "image/jpeg"
        case "png":
            ext = "image/png"
        case "pdf":
            ext = "application/pdf"
        case "txt":
            ext = "text/plain"
        case "zip":
            ext = "application/zip"
        case _:
            ext = "application/octet-stream"

    print(ext)

main()
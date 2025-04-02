import flet as ft

def main(page: ft.Page):
    page.title = "Hello world with Flet!!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    page.update()
    
    def upload_files(e):
        upload_list = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                upload_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(upload_list)

    chose_file_button = ft.ElevatedButton("Upload", on_click=upload_files)

    page.add(chose_file_button)

    page.update()


ft.app(target=main)
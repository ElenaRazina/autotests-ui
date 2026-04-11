from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.views.empty_view_component import EmptyViewComponent
from elements.file_input import FileInput
from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from elements.file_input import FileInput

class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page,identifier: str):
        super().__init__(page)

        self.preview_empty_view=EmptyViewComponent(page,identifier)
        #self.preview_image = page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')
        #self.preview_image_upload_info_icon = page.get_by_test_id(f'{identifier}-image-upload-widget-info-icon')
        #self.preview_image_upload_info_title = page.get_by_test_id(f'{identifier}-image-upload-widget-info-title-text')
        #self.preview_image_upload_info_description = page.get_by_test_id(f'{identifier}-image-upload-widget-info-description-text')
        #self.upload_button = page.get_by_test_id(f'{identifier}-image-upload-widget-upload-button')
        #self.remove_button = page.get_by_test_id(f'{identifier}-image-upload-widget-remove-button')
        #self.upload_input = page.get_by_test_id(f'{identifier}-image-upload-widget-input')

        self.preview_image=Icon(page, f'{identifier}-image-upload-widget-preview-image', 'Preview image')
        self.preview_image_upload_info_icon=Icon(page, f'{identifier}-image-upload-widget-info-icon', 'Preview image upload info icon')
        self.preview_image_upload_info_title=Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Preview image upload info title')
        self.preview_image_upload_info_description=Text(page, f'{identifier}-image-upload-widget-info-description-text', 'Preview image upload info description')
        self.upload_button=Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload button')
        self.remove_button=Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove button')
        self.upload_input=FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload input')


    def check_visible(self, is_image_uploaded: bool = False):
        #expect(self.preview_image_upload_info_icon).to_be_visible()
        self.preview_image_upload_info_icon.check_visible()

        #expect(self.preview_image_upload_info_title).to_be_visible()
        #expect(self.preview_image_upload_info_title).to_have_text('Tap on "Upload image" button to select file')
        self.preview_image_upload_info_title.check_visible()
        self.preview_image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')


        #expect(self.preview_image_upload_info_description).to_be_visible()
        #expect(self.preview_image_upload_info_description).to_have_text('Recommended file size 540X300')
        self.preview_image_upload_info_description.check_visible()
        self.preview_image_upload_info_description.check_have_text('Recommended file size 540X300')


        #expect(self.upload_button).to_be_visible()
        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.preview_image.check_visible()
        #    expect(self.remove_button).to_be_visible()
        #    expect(self.preview_image).to_be_visible()


        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here')

    def click_remove_image_button(self):
        self.remove_button.click()

    def check_visible_preview_image(self):
        #expect(self.preview_image).to_be_visible()
        self.preview_image.check_visible()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)



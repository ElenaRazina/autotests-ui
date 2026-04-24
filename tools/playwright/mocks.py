from playwright.sync_api import Route,Page

#def abort(route:Route):
    # Временно печатаем ссылку на отключаемый ресурс
    #print(f"\nAborting url: {route.request.url}")
    # Отменяем загрузку ресурса
    #route.abort()

def mock_static_resources(page:Page):
    # Отключаем загрузку статических ресурсов
    #page.route("**/*.{ico,png,jpg,svg,webp,mp3,mp4,woff,woff2}", abort)
    page.route(
        "**/*.{ico,png,jpg,webp,mp3,mp4,woff,woff2}",
        lambda
            route: route.abort())


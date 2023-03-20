from pydantic import BaseSettings


class Settings(BaseSettings):
    app_environment = 'dev'
    client_hostname: str = '' #set this to your websites hostname
    nomic_api_key: str = ''  #set this to your Nomic API key (atlas.nomic.ai/cli-login)
    atlas_project_name: str = ''
    openai_api_key = str = ''


settings = Settings()

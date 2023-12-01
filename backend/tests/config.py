import pydantic
import pydantic_settings


class TestSettings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    ugc_protocol: str = pydantic.Field(default="http", alias="UGC_PROTOCOL")
    ugc_host: str = pydantic.Field(default="localhost", alias="UGC_HOST")

    jwt_secret_key: str = pydantic.Field(..., alias="JWT_SECRET_KEY")
    jwt_algorithm: str = pydantic.Field("HS256", alias="TOKEN_SIGN_ALGORITHM")

    def get_ugc_url(self):
        return f"{self.ugc_protocol}://{self.ugc_host}/api/v1/events/"


tests_settings = TestSettings()

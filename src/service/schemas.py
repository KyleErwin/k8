from enum import Enum

from pydantic import BaseModel, Field


class JobEnum(str, Enum):
    admin = "admin"
    blue_collar = "blue-collar"
    entrepreneur = "entrepreneur"
    housemaid = "housemaid"
    management = "management"
    retired = "retired"
    self_employed = "self-employed"
    services = "services"
    student = "student"
    technician = "technician"
    unemployed = "unemployed"
    unknown = "unknown"


class MaritalEnum(str, Enum):
    married = "married"
    single = "single"
    divorced = "divorced"


class EducationEnum(str, Enum):
    primary = "primary"
    secondary = "secondary"
    tertiary = "tertiary"
    unknown = "unknown"


class PreviouslyContactedEnum(str, Enum):
    never = "never"
    within_a_week = "within_a_week"
    within_a_month = "within_a_month"
    over_a_month = "over_a_month"


class PreviousCampaignOutcomeEnum(str, Enum):
    failure = "failure"
    other = "other"
    success = "success"
    unknown = "unknown"


class PredictionRequest(BaseModel):
    age: int = Field(..., ge=18, le=100)
    balance: float
    default: bool
    housing: bool
    loan: bool
    campaign: int = Field(..., ge=1)
    job: JobEnum
    marital: MaritalEnum
    education: EducationEnum
    previous: int = Field(..., ge=1)
    pcontacted: PreviouslyContactedEnum
    poutcome: PreviousCampaignOutcomeEnum

    def to_model_input(self) -> dict:
        return {
            "age": self.age,
            "balance": self.balance,
            "default": int(self.default),
            "housing": int(self.housing),
            "loan": int(self.loan),
            "campaign": self.campaign,
            "job": self.job.value,
            "marital": self.marital.value,
            "education": self.education.value,
            "pcontacted": self.pcontacted.value,
            "previous": self.previous,
            "poutcome": self.poutcome.value,
        }


class PredictionResponse(BaseModel):
    prediction: str

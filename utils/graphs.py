from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List

# from datetime import date,datetime
from utils.llms import llm
from utils.prompt import ats_prompt


class JobDetails(TypedDict):
    title: str
    company: str


class Candidate(TypedDict):
    certifications: List[str]
    issuing_authority: List[str]
    date_earned: List[str]
    platform_link: List[str]


class DashboardState(TypedDict):
    resume_text: str
    job_desc: str
    job_details: JobDetails
    candidate_details: Candidate
    analysis_quote: List[str]
    readiness_score: float
    ats_score: float

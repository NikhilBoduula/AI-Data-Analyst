from backend.agents.execution_agent import ExecutionAgent
from backend.agents.decision_agent import DecisionAgent
from backend.intelligence.reasoning_engine import ReasoningEngine
from backend.intelligence.dataset_intelligence import DatasetIntelligence
from backend.intelligence.quality_intelligence import QualityIntelligence
from backend.intelligence.model_intelligence import ModelIntelligence
from backend.intelligence.explainability_intelligence import (
    ExplainabilityIntelligence,
)
from backend.intelligence.recommendation_intelligence import (
    RecommendationIntelligence,
)
from backend.intelligence.executive_summary import ExecutiveSummary


class BusinessAgent:

    @staticmethod
    def generate(
        dataset,
        automl_results=None,
        shap_results=None,
    ):

        # =====================================================
        # Intelligence Modules
        # =====================================================

        dataset_info = DatasetIntelligence.analyze(
            dataset
        )

        quality_info = QualityIntelligence.analyze(
            dataset
        )

        model_info = ModelIntelligence.analyze(
            automl_results
        )

        explainability_info = (
            ExplainabilityIntelligence.analyze(
                shap_results
            )
        )

        recommendation_info = (
            RecommendationIntelligence.analyze(
                dataset_info,
                quality_info,
                model_info,
                explainability_info
            )
        )

        reasoning = (
            ReasoningEngine.analyze(
                dataset_info,
                quality_info,
                model_info,
                explainability_info,
                recommendation_info
            )
        )

        decisions = DecisionAgent.decide(
            dataset_info,
            quality_info,
            model_info,
            explainability_info,
            recommendation_info
        )

        execution = ExecutionAgent.execute(
            quality_info,
            model_info,
            explainability_info,
            recommendation_info
        )

        executive_summary = (
            ExecutiveSummary.generate(
                dataset_info,
                quality_info,
                model_info,
                explainability_info,
                recommendation_info
            )
        )

        # =====================================================
        # Return Complete Intelligence
        # =====================================================

        return [
            executive_summary,
            reasoning,
            {
                "title": "🤖 AI Decisions",
                "message": decisions
            },
            execution,
            dataset_info,
            quality_info,
            model_info,
            explainability_info,
            recommendation_info,
        ]
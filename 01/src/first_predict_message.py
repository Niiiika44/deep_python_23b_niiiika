from src.first_model import SomeModel


class LogicError(Exception):
    "Invalid thresholds"


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    cond_1 = not isinstance(message, str)
    cond_2 = not isinstance(model, SomeModel)
    cond_3 = type(bad_thresholds) not in (int, float)
    cond_4 = type(good_thresholds) not in (int, float)

    if cond_1 or cond_2 or cond_3 or cond_4:
        raise TypeError
    if bad_thresholds >= good_thresholds:
        raise LogicError
    if not hasattr(model, "predict"):
        raise AttributeError

    prediction = model.predict(message)

    if prediction < bad_thresholds:
        return "неуд"
    elif prediction > good_thresholds:
        return "отл"
    else:
        return "норм"

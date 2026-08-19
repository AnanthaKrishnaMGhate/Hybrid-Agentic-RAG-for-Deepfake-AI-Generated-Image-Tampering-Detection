import pandas as pd


def load_dataset():
    fake_df = pd.read_csv("data/Fake.csv", encoding="utf-8")
    true_df = pd.read_csv("data/True.csv", encoding="utf-8")

    fake_df["label"] = "Fake"
    true_df["label"] = "Real"

    df = pd.concat([fake_df, true_df], ignore_index=True)

    df["content"] = (
        fake_df["title"].fillna("") + " " +
        fake_df["text"].fillna("")
    )

    return df
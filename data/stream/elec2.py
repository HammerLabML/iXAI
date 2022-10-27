from river.datasets import Elec2 as RiverDataset
from data.stream._base import StreamDataset


class Elec2(StreamDataset):

    def __init__(
            self,
            n_samples: int = 45312
    ):
        stream = RiverDataset()
        feature_names = ['date', 'day', 'period', 'nswprice', 'nswdemand', 'vicprice', 'vicdemand', 'transfer']
        cat_feature_names = []
        num_feature_names = feature_names
        super().__init__(
            stream=stream,
            n_samples=n_samples,
            feature_names=feature_names,
            cat_feature_names=cat_feature_names,
            num_feature_names=num_feature_names,
            task=stream.task,
            n_features=len(feature_names),
            n_outputs=stream.n_outputs,
        )


if __name__ == "__main__":
    dataset = Elec2()
    stream = dataset.stream
    print(stream.n_samples)
    for n, (x_i, y_i) in enumerate(stream):
        print(n, x_i, y_i)
        if n > 3:
            print("\n", dataset.feature_names, "\n", list(x_i.keys()))
            break

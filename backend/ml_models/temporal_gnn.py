import torch

from torch_geometric_temporal.nn.recurrent import GConvGRU


class TemporalRiskGNN(torch.nn.Module):

    def __init__(self):

        super().__init__()

        self.recurrent = GConvGRU(

            in_channels=3,

            out_channels=16,

            K=2
        )


    def forward(

        self,

        x,

        edge_index,

        edge_weight
    ):

        h = self.recurrent(

            x,

            edge_index,

            edge_weight
        )

        return h
import torch

from torch_geometric.data import Data

from backend.ml_models.gnn_model import RiskGNN


x = torch.tensor([

    [0.8, 0.7, 0.6],
    [0.5, 0.4, 0.3],
    [0.9, 0.8, 0.7],
    [0.3, 0.2, 0.1]

], dtype=torch.float)


edge_index = torch.tensor([

    [0, 1, 2, 3],
    [1, 0, 3, 2]

], dtype=torch.long)


data = Data(x=x, edge_index=edge_index)


model = RiskGNN()

output = model(data)

print(output)
import torch
import torch.nn.functional as F

from torch import nn

class Attention(nn.Module):
	"""
	Inputs:
		last_hidden: (batch_size, hidden_size)
		encoder_outputs: (batch_size, max_time, hidden_size)
	Returns:
		attention_weights: (batch_size, max_time)
	"""
	def __init__(self, batch_size, hidden_size, method="dot", mlp=False):
		super(Attention, self).__init__()
			self.method = method
			self.hidden_size = hidden_size

			if method == 'dot':
				pass
			elif method == 'general':
				self.Wa = nn.Linear(hidden_size, hidden_size, bias=False)
			elif method == 'concat':
				self.Wa = nn.Linear(hidden_size, hidden_size, bias=False)
				self.va = nn.Parameter(torch.FloatTensor(batch_size, hidden_size))
			elif method == 'bahdanau':
				self.Wa = nn.Linear(hidden_size, hidden_size, bias=False)
				self.Ua = nn.Linear(hidden_size, hidden_size, bias=False)
				self.va = nn.Parameter(torch.FloatTensor(batch_size, hidden_size))
			else:
				raise NotImplementedError

			self.mlp = mlp
			if mlp:
				self.phi = nn.Linear(hidden_size, hidden_size, bias=False)
				self.psi = nn.Linear(hidden_size, hidden_size, bias=False)

	def forward(self, last_hidden, encoder_outputs, seq_len=None):
		batch_size, seq_lens, _ = encoder_outputs.size()
		if self.mlp:
			last_hidden = self.phi(last_hidden)
			encoder_outputs = self.psi(encoder_outputs)

		attention_energies = self._score(last_hidden, encoder_outputs, self.method)

		if seq_len is not None:
			attention_energies = mask_3d(attention_energies, seq_len, -float('inf'))

		return F.softmax(attention_energies, -1)

	def _score(self, last_hidden, encoder_outputs, method):
		"""
		Computes an attention score
		:param last_hidden: (batch_size, hidden_dim)
		:param encoder_outputs: (batch_size, max_time, hidden_dim)
		:param method: str (`dot`, `general`, `concat`, `bahdanau`)
		:return: a score (batch_size, max_time)
		"""

		assert encoder_outputs.size()[-1] == self.hidden_size

		if method == 'dot':
			last_hidden = last_hidden.unsqueeze(-1)
			return encoder_outputs.bmm(last_hidden).squeeze(-1)

		elif method == 'general':
			x = self.Wa(last_hidden)
			x = x.unsqueeze(-1)
			return encoder_outputs.bmm(x).squeeze(-1)

		elif method == "concat":
			x = last_hidden.unsqueeze(1)
			x = F.tanh(self.Wa(torch.cat((x, encoder_outputs), 1)))
			return x.bmm(self.va.unsqueeze(2)).squeeze(-1)

		elif method == "bahdanau":
			x = last_hidden.unsqueeze(1)
			out = F.tanh(self.Wa(x) + self.Ua(encoder_outputs))
			return out.bmm(self.va.unsqueeze(2)).squeeze(-1)

		else:
			raise NotImplementedError

	def extra_repr(self):
		return f'score={self.method}, mlp_preprocessing={self.mlp}'

if __name__ == "__main__":
	print('running attention.py')

	torch.manual_seed(0)
	device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
	cnn_encoder = RNN().to(device)
	tensor = torch.rand(size=(8, 1, 20, 20)).to(device)
	latent_rep, _, channel_size, img_size = cnn_encoder.forward(tensor)

	print(cnn_encoder)
	print(latent_rep)
	print(f'''
	      out channel_size: {channel_size},
	      out img_size: {img_size}
	      ''')

	print('done.')

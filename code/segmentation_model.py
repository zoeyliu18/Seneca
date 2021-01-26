import opennmt
import tensorflow as tf
import tensorflow_addons as tfa

class Seneca(opennmt.models.SequenceToSequence):

    def __init__(self):
        super().__init__(
            source_inputter=opennmt.inputters.WordEmbedder(embedding_size=300),
            target_inputter=opennmt.inputters.WordEmbedder(embedding_size=300),
            encoder=opennmt.encoders.RNNEncoder(
                num_layers=2,
                num_units=128,
                bidirectional=True,
                residual_connections=False,
                dropout=0.1,
                reducer=opennmt.layers.ConcatReducer(),
                cell_class=tf.keras.layers.LSTMCell,
            ),
            decoder=opennmt.decoders.AttentionalRNNDecoder(
                num_layers=2,
                num_units=128,
                bridge_class=opennmt.layers.CopyBridge,
                attention_mechanism_class=tfa.seq2seq.LuongAttention,
                attention_layer_activation=None,
                cell_class=tf.keras.layers.LSTMCell,
                dropout=0.1,
                residual_connections=False,
            ),
            share_embeddings=opennmt.models.EmbeddingsSharingLevel.ALL
        )

model = Seneca
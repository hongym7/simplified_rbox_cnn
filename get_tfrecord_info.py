import tensorflow as tf


def get_tfrecords_feature_list(tfrecords_filename):
    ptr = 0
    record_iterator = tf.python_io.tf_record_iterator(path=tfrecords_filename)

    for string_record in record_iterator:
        example = tf.train.Example()
        example.ParseFromString(string_record)

        print(example)
        return example.features.feature.keys()

    return []


if __name__ == '__main__':
    print('bbb')
    get_tfrecords_feature_list('/mnt/disk2/dl_data/Arirang_Dataset/train.tfrecord')
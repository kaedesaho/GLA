import matplotlib.pyplot as plt

def plot(COST, ACC):
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.plot(COST, color=color)
    ax1.set_xlabel('epoch', color=color)
    ax1.set_ylabel('total loss', color=color)
    ax1.tick_params(axis='y', color=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.plot(ACC, color=color)
    ax2.set_ylabel('accuracy', color=color)
    ax2.tick_params(axis='y', color=color)
    fig.tight_layout()

    plt.show()

def plot_loss_acc(epochs, total_loss_list, acc_epoch):
    epochs_range = range(1, epochs + 1)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, total_loss_list, marker='o', label='Training Loss')
    plt.title('Training Loss per Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, acc_epoch, marker='o', color='green', label='Validation Accuracy')
    plt.title('Validation Accuracy per Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    
    
def plot_train_val(epochs, train_loss, val_loss, train_acc, val_acc):
    epochs_range = range(1, epochs + 1)

    # Plot Loss
    plt.figure(figsize=(10, 4))
    plt.plot(epochs_range, train_loss, label='Train Loss', marker='o')
    plt.plot(epochs_range, val_loss, label='Validation Loss', marker='o')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss over Epochs')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot Accuracy
    plt.figure(figsize=(10, 4))
    plt.plot(epochs_range, train_acc, label='Train Accuracy', marker='o')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy', marker='o')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Accuracy over Epochs')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    // PAUSED @ https://youtu.be/050zzD4c-5c?t=5495

    return a.exec();
}

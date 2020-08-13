#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "custombutton.h"
#include <QHBoxLayout>
#include <QVBoxLayout>

#include "customwidget.h"

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:

    void onClickCustomBtn();

private:
    // "m_" added for "Main attribute"
    QPushButton* m_customBtnBonjour;

    QWidget* m_mainWidget;

    QVBoxLayout* m_vBoxLayout;
    QHBoxLayout* m_hBoxLayout;
};

#endif // MAINWINDOW_H

#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "custombutton.h"   //added
#include <QHBoxLayout>      //added
#include <QVBoxLayout>      //added

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
    QPushButton* m_customBtnBonjour;   // added ("m_" for Main attr)

    QWidget* m_mainWidget;

    QVBoxLayout* m_vBoxLayout;   // added ("m_" for Main attr)
    QHBoxLayout* m_hBoxLayout;   // added ("m_" for Main attr)
};

#endif // MAINWINDOW_H

Attribute VB_Name = "Module1"
'
' This challenge is very similar to others found on the internet, so
' I have used my google-foo skills to find solutions.
'


Sub ticker_loop()
    On Error Resume Next

' Define variables
    Dim ws_count As Integer
    Dim i As Integer
    Dim j As Long
    Dim k As Integer
    Dim l As Integer
    Dim m As Integer
    Dim total_vol As Double
    Dim open_price_beginning As Double
    Dim close_price_end As Double

' Set counter
    k = 2  'start on row 2
    ws_count = ActiveWorkbook.Worksheets.Count  'count number of worksheets in workbook

' Set worksheet loop
    For i = 1 To ws_count

' Label columns in the aggregated ticker chart
        ActiveWorkbook.Worksheets(i).Cells(1, 9).Value = "Ticker"
        ActiveWorkbook.Worksheets(i).Cells(1, 10).Value = "Yearly Change"
        ActiveWorkbook.Worksheets(i).Cells(1, 11).Value = "Percent Change"
        ActiveWorkbook.Worksheets(i).Cells(1, 12).Value = "Total Stock Volume"


' Label columns in the summary chart
        ActiveWorkbook.Worksheets(i).Cells(1, 16).Value = "Ticker"
        ActiveWorkbook.Worksheets(i).Cells(1, 17).Value = "Value"
        ActiveWorkbook.Worksheets(i).Cells(2, 15).Value = "Greatest % Increase"
        ActiveWorkbook.Worksheets(i).Cells(3, 15).Value = "Greatest % Decrease"
        ActiveWorkbook.Worksheets(i).Cells(4, 15).Value = "Greatest Total Volume"

' Set volume equal to zero since we're summing over a range
        total_vol = 0

' Loop over the entire sheet
        For j = 2 To ActiveWorkbook.Worksheets(i).Cells.SpecialCells(xlCellTypeLastCell).Row
            If ActiveWorkbook.Worksheets(i).Cells(j, 1).Value <> ActiveWorkbook.Worksheets(i).Cells(j + 1, 1).Value Then

' Loops through each sheet to find difference and percentage changes for each ticker
                close_price_end = ActiveWorkbook.Worksheets(i).Cells(j, 6).Value
                ActiveWorkbook.Worksheets(i).Cells(k, 10).Value = close_price_end - open_price_beginning
                ActiveWorkbook.Worksheets(i).Cells(k, 11).Value = (close_price_end - open_price_beginning) / open_price_beginning
                open_price_beginning = 0
                close_price_end = 0

' Loops through each sheet to sum the "vol" columns for each ticker
                ActiveWorkbook.Worksheets(i).Cells(k, 9).Value = ActiveWorkbook.Worksheets(i).Cells(j, 1).Value
                total_vol = total_vol + ActiveWorkbook.Worksheets(i).Cells(j, 7).Value
                ActiveWorkbook.Worksheets(i).Cells(k, 12).Value = total_vol
                k = k + 1
                total_vol = 0
            ElseIf ActiveWorkbook.Worksheets(i).Cells(j - 1, 1).Value <> ActiveWorkbook.Worksheets(i).Cells(j, 1).Value Then

' Loops through each sheet to find difference and percentage changes for each ticker
                open_price_beginning = ActiveWorkbook.Worksheets(i).Cells(j, 3).Value

' Loops through each sheet to sum the "vol" columns for each ticker
                total_vol = total_vol + ActiveWorkbook.Worksheets(i).Cells(j, 7).Value
            Else

' Loops through each sheet to sum the "vol" columns for each ticker
                total_vol = total_vol + ActiveWorkbook.Worksheets(i).Cells(j, 7).Value
            End If
        Next j

' Summary Chart -- find maximum % increase, % decrease, and total volume
        ActiveWorkbook.Worksheets(i).Cells(2, 17).Value = WorksheetFunction.Max(Worksheets(i).Range("K2:K" & ActiveWorkbook.Worksheets(i).Range("I2").CurrentRegion.Rows.Count))
        ActiveWorkbook.Worksheets(i).Cells(3, 17).Value = WorksheetFunction.Min(Worksheets(i).Range("K2:K" & ActiveWorkbook.Worksheets(i).Range("I2").CurrentRegion.Rows.Count))
        ActiveWorkbook.Worksheets(i).Cells(4, 17).Value = WorksheetFunction.Max(Worksheets(i).Range("L2:L" & ActiveWorkbook.Worksheets(i).Range("I2").CurrentRegion.Rows.Count))

' Summary Chart -- Format datatypes to be percentages
        ActiveWorkbook.Worksheets(i).Cells(2, 17).Style = "Percent"
        ActiveWorkbook.Worksheets(i).Cells(3, 17).Style = "Percent"

' Summary Chart -- Find Tickers for mins & maxs
        For l = 2 To ActiveWorkbook.Worksheets(i).Range("K1").CurrentRegion.Rows.Count
            If ActiveWorkbook.Worksheets(i).Cells(l, 11).Value = ActiveWorkbook.Worksheets(i).Cells(2, 17).Value Then
                ActiveWorkbook.Worksheets(i).Cells(2, 16).Value = ActiveWorkbook.Worksheets(i).Cells(l, 9).Value
            ElseIf ActiveWorkbook.Worksheets(i).Cells(l, 11).Value = ActiveWorkbook.Worksheets(i).Cells(3, 17).Value Then
                ActiveWorkbook.Worksheets(i).Cells(3, 16).Value = ActiveWorkbook.Worksheets(i).Cells(l, 9).Value
            ElseIf ActiveWorkbook.Worksheets(i).Cells(l, 12).Value = ActiveWorkbook.Worksheets(i).Cells(4, 17).Value Then
                ActiveWorkbook.Worksheets(i).Cells(4, 16).Value = ActiveWorkbook.Worksheets(i).Cells(l, 9).Value
            End If
        Next l

' Formatting -- column shading for new aggregate and summary charts
        With ActiveWorkbook.Worksheets(i).Range("I1:J1").CurrentRegion.Interior
            .ThemeColor = xlThemeColorDark1
            .TintAndShade = -0.2
        End With

        With ActiveWorkbook.Worksheets(i).Range("P1:Q4").CurrentRegion.Interior
            .ThemeColor = xlThemeColorDark1
            .TintAndShade = -0.2
        End With

' Formatting -- column headers for new aggregate and summary charts
        With ActiveWorkbook.Worksheets(i).Range("I1:L1", "P1:Q1")
            .Font.Bold = True
            .HorizontalAlignment = xlCenter
        End With

' Formatting -- makes positive changes green and negative changes red
        For m = 2 To ActiveWorkbook.Worksheets(i).Range("K1").CurrentRegion.Rows.Count
            ActiveWorkbook.Worksheets(i).Cells(m, 11).Style = "Percent"
            If ActiveWorkbook.Worksheets(i).Cells(m, 10).Value > 0 Then
                With ActiveWorkbook.Worksheets(i).Cells(m, 10).Interior
                    .ColorIndex = 4
                    .TintAndShade = 0.6
                End With
            Else
                With ActiveWorkbook.Worksheets(i).Cells(m, 10).Interior
                    .ColorIndex = 3
                    .TintAndShade = 0.6
                End With
            End If
        Next m
        

' Sets k = 2 so that the loop can start again on a new sheet with the table at the top of the sheet
        k = 2
    Next i
  
End Sub

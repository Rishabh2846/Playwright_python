import { test, expect } from '@playwright/test';

test('Web Inputs', async ({ page }) => {


await page.goto('https://practice.expandtesting.com/inputs');

await page.getByRole('spinbutton', { name: 'Input: Number' }).fill('123455');

await page.getByRole('textbox', { name: 'Input: Text' }).fill('test');
await page.getByRole('textbox', { name: 'Input: Text' }).press('Tab');
await page.getByRole('textbox', { name: 'Input: Password' }).fill('admin');
await page.getByRole('textbox', { name: 'Input: Date' }).fill('2025-08-30');
await page.getByRole('button', { name: 'Display Inputs' }).click();
await expect(page.getByText('123455')).toBeVisible();
await expect(page.getByText('test', { exact: true })).toBeVisible();
await expect(page.getByText('admin')).toBeVisible();
await expect(page.getByText('-08-30')).toBeVisible();
await page.getByRole('button', { name: 'Clear Inputs' }).click();
});